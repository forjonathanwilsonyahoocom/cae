import sys
import os
import yaml  # Expected in the dev environment for YAML parsing

class TopologyValidationError(Exception):
    """Raised when the multi-agent layout violates architectural bounds."""
    pass

def validate_topology(config_path):
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Missing required topology file: {config_path}")

    with open(config_path, 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as e:
            raise TopologyValidationError(f"Invalid YAML syntax: {e}")

    # 1. Structural Schema Assertions
    assert config.get("version") == "cae.v1alpha", "Unsupported layout schema version."
    
    metadata = config.get("metadata", {})
    subsystem = metadata.get("subsystem_name", "unknown")
    topology_type = metadata.get("declared_topology")
    
    agents = config.get("agents", {})
    matrix = config.get("communication_matrix", {})
    allowed_routes = matrix.get("allowed_routes", [])
    forbidden_routes = matrix.get("forbidden_routes", [])

    print(f"[*] Validating '{subsystem}' ({topology_type} topology)...")

    # 2. Orphan Node Validation
    # Ensure every single declared agent actually has an active route definition
    routed_agents = set()
    for route in allowed_routes:
        routed_agents.add(route.get("from"))
        for target in route.get("to", []):
            routed_agents.add(target)

    for agent_name in agents:
        if agent_name not in routed_agents:
            raise TopologyValidationError(
                f"Orphan Node Found: Agent '{agent_name}' is declared but completely missing from the communication_matrix."
            )

    # 3. Explicit Forbidden Route Verification
    # Parse concrete edge code paths at runtime to intercept illicit mesh communication
    for forbidden in forbidden_routes:
        f_from = forbidden.get("from")
        f_to = forbidden.get("to")
        reason = forbidden.get("reason", "No reason provided.")

        for allowed in allowed_routes:
            if allowed.get("from") == f_from and f_to in allowed.get("to", []):
                raise TopologyValidationError(
                    f"Architectural Contradiction in '{subsystem}':\n"
                    f"Route '{f_from} -> {f_to}' is explicitly forbidden, but listed under allowed_routes.\n"
                    f"Reason for ban: {reason}"
                )

    # 4. Strict Topology Rule Enforcement
    if topology_type == "star":
        # In a star layout, non-orchestrator agents must never directly communicate
        # Look for any allowed route where a worker bypasses the primary hub
        for allowed in allowed_routes:
            sender = allowed.get("from")
            targets = allowed.get("to", [])
            if sender != "orchestrator":
                for target in targets:
                    if target != "orchestrator":
                        raise TopologyValidationError(
                            f"Topology Defiance: Mesh leak found in Star architecture.\n"
                            f"Worker agent '{sender}' is attempting to message worker agent '{target}' directly."
                        )

    print("[+] Topology validation successful. No architectural leaks detected.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_topology.py <path_to_topology.yaml>")
        sys.exit(1)
        
    try:
        validate_topology(sys.argv[1])
        sys.exit(0)
    except TopologyValidationError as err:
        print(f"\n[!] ARCHITECTURAL VIOLATION: {err}\n", file=sys.stderr)
        sys.exit(1)

