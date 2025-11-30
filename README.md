# AI Study Planner

## Background

Students often struggle to create consistent, optimized study plans that match their goals, deadlines, learning styles, and available time. Traditional timetable templates are rigid and do not adapt when circumstances change. Many learners waste time deciding what to study every day instead of actually studying.

With the growth of AI models, it has become possible to build intelligent agents that can understand student goals, break them into manageable tasks, create daily or weekly schedules, recommend learning resources, and evaluate progress.

AI Study Planner solves this problem using a multi-agent AI system capable of understanding the student, planning efficiently, improving itself, and adapting as the student progresses.

## Project Narrative

AI Study Planner is designed as a collaborative multi-agent system that works like an intelligent digital study coach.

The system is built from several agents:

- Profile and memory layer
- Study Planner Agent
- Research Agent
- Evaluation Agent
- Orchestrator Agent

The Study Planner Agent creates a day-by-day plan using a custom time allocation tool. The Research Agent suggests resources for each subject. The Evaluation Agent scores the plan and suggests improvements. The Orchestrator coordinates all agents and produces the final plan.

## Architecture

```mermaid
flowchart TD

    User([User Input])

    subgraph Memory[Memory Layer]
        SM(Session Memory)
        LTM(Long-Term Memory)
    end

    subgraph Agents[Multi-Agent System]
        O[Orchestrator Agent]
        P[Study Planner Agent]
        R[Research Agent]
        E[Evaluation Agent]
    end

    subgraph Tools[Tools Layer]
        TT[Time Calculation Tool]
        ST[Search Tool]
    end

    User --> O

    O --> SM
    O --> LTM

    O --> P
    P --> TT

    O --> R
    R --> ST

    O --> E
    E --> O

    O --> User

