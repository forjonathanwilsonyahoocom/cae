# CAE Law 1: Structure Precedes Computation

## Statement

Every autonomous system should establish an explicit representation
of the problem space before allocating significant computational effort.

- structure before search
- constrain exploration before expensive computation
- classify before modeling
- define measurements before changing systems
- establish context before reasoning

## Rationale

Unstructured computation expands the search space faster than it
expands understanding.

## Evidence

Examples from:

- distributed systems
- scientific workflows
- debugging
- incident response
- autonomous agents

## Counterexamples

Cases where structure emerged after computation.

## Open Questions

When can computation discover better structures?

# CAE Law 2: Diagnose Before Retry

## Statement

Every autonomous system should identify the failed stage of a process before allocating additional computation toward repetition.

Retries without diagnosis increase activity without necessarily increasing understanding.

A system should distinguish whether failure originated from:

* mission definition
* policy selection
* execution variance
* verification strategy
* telemetry insufficiency
* environmental assumptions

before attempting correction.

## Principles

* failure classification precedes remediation
* new computation should be justified by a falsifiable hypothesis
* repeated execution without changed assumptions is not iteration
* feedback should modify the mechanism that produced failure, not merely repeat the request

## Rationale

Undiagnosed retries consume computational resources while preserving the conditions that caused failure.

In human engineering, debugging, incident response, and scientific investigation, progress comes from identifying the mechanism of failure. Autonomous systems require the same discipline.

A failed attempt is not merely a reason to try harder. It is evidence about which part of the system's model, policy, or execution path was insufficient.

## Evidence

Examples from:

* software debugging
* distributed systems incident response
* scientific experimentation
* aviation and safety engineering
* machine learning evaluation
* autonomous agent workflows

Common failure pattern:

```
Attempt fails
    ↓
Retry with more effort
    ↓
Different failure occurs
    ↓
Additional instructions accumulate
    ↓
System becomes less diagnosable
```

CAE replaces this with:

```
Attempt fails
    ↓
Classify failure stage
    ↓
Form falsifiable hypothesis
    ↓
Modify policy or assumptions
    ↓
Measure outcome
```

## Counterexamples

Cases where retries are appropriate:

* transient infrastructure failures
* stochastic execution variance
* external dependencies with known instability
* exploration where the objective is explicitly sampling outcomes

In these cases, retrying is itself the correct policy because the failure mechanism is already understood.

## Relationship to Other CAE Laws

**Law 1: Structure Precedes Computation**

Structure defines the space in which computation operates.

**Law 2: Diagnose Before Retry**

Diagnosis determines how computation should adapt after encountering reality.

Together:

```
Structure → Computation → Diagnosis → Adaptation
```

## Open Questions

* How much diagnosis is required before retry becomes wasteful?
* Can autonomous systems learn reusable failure classifications?
* What telemetry is minimally sufficient for reliable diagnosis?
* When should an agent choose exploration over diagnosis?
* Can failure diagnosis itself be budgeted as a computational resource?

