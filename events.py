# Event library defining 12 rounds with options.
# Each option can affect sentiment, budget, adoption, and diffusion parameters.

EVENT_LIBRARY = [
    {
        "title":"CEO Mandate: AI Everywhere",
        "description":"The CEO sets a bold goal: enterprise-wide AI adoption within 18 months. Employees are curious but unsure.",
        "options":[
            {
                "label":"Hold live video town hall with Q&A",
                "detail":"High-reach communication. Leadership visible and accountable.",
                "cost":100_000,
                "units":["Enterprise"],
                "effects":[{"type":"sentiment","value":3},{"type":"p_adjust","value":0.005,"target":"enterprise"}],
                "note":"Boosts trust; small innovation bump."
            },
            {
                "label":"Launch AI Champions in IT & Sales",
                "detail":"Identify and empower influential early adopters.",
                "cost":200_000,
                "units":["IT & Data Science","Sales & Marketing"],
                "effects":[
                    {"type":"q_adjust","value":0.05,"target":["IT & Data Science","Sales & Marketing"]},
                    {"type":"adoption_boost","value":5,"target":["IT & Data Science","Sales & Marketing"]}
                ],
                "note":"Peer influence increases imitation coefficient."
            },
            {
                "label":"Departmental training for Customer Service",
                "detail":"Focused training sprints, hands-on use cases.",
                "cost":500_000,
                "units":["Customer Service"],
                "effects":[
                    {"type":"adoption_boost","value":8,"target":["Customer Service"]},
                    {"type":"p_adjust","value":0.01,"target":["Customer Service"]}
                ]
            },
        ]
    },
    {
        "title":"Rumors of Layoffs in Operations",
        "description":"A Slack thread suggests AI will cut frontline jobs. Anxiety rises.",
        "options":[
            {
                "label":"Address rumors in open forum",
                "detail":"Transparent Q&A with Ops leadership; commit to reskilling.",
                "cost":50_000,
                "units":["Operations"],
                "effects":[{"type":"sentiment","value":5},{"type":"q_adjust","value":0.03,"target":["Operations"]}]
            },
            {
                "label":"Reskilling guarantee",
                "detail":"Formal policy to retrain impacted roles with job placement.",
                "cost":200_000,
                "units":["Operations"],
                "effects":[{"type":"sentiment","value":10},{"type":"p_adjust","value":0.005,"target":["Operations"]}]
            },
            {
                "label":"Ignore the rumors",
                "detail":"Hope it blows over.",
                "cost":0,
                "units":["Operations"],
                "effects":[{"type":"sentiment","value":-5},{"type":"q_adjust","value":-0.03,"target":["Operations"]}],
                "risks":"Backlash may spread to other units."
            },
        ]
    },
    {
        "title":"Competitor Automates Customer Service",
        "description":"A rival reports 15% cost reduction with AI in Customer Service.",
        "options":[
            {
                "label":"Rally the org with benchmarking",
                "detail":"Communicate competitive urgency enterprise-wide.",
                "cost":50_000,
                "effects":[{"type":"sentiment","value":2},{"type":"q_adjust","value":0.02,"target":"enterprise"}]
            },
            {
                "label":"Fast-track chatbot pilot in Customer Service",
                "detail":"Stand up a supervised AI chatbot pilot with guardrails.",
                "cost":1_000_000,
                "units":["Customer Service"],
                "effects":[{"type":"adoption_boost","value":15,"target":["Customer Service"]},{"type":"p_adjust","value":0.01,"target":["Customer Service"]}],
                "risks":"Operational hiccups possible in early rollout."
            },
            {
                "label":"Focus on internal productivity (Finance & HR)",
                "detail":"Automation of workflows, document drafting, reconciliations.",
                "cost":750_000,
                "units":["Finance & Legal","HR & Learning"],
                "effects":[{"type":"adoption_boost","value":10,"target":["Finance & Legal","HR & Learning"]}]
            },
        ]
    },
    {
        "title":"Legal Raises Risk Concerns",
        "description":"Counsel flags data privacy and IP leakage risks with AI tools.",
        "options":[
            {
                "label":"Establish AI governance & guardrails",
                "detail":"Usage policy, data retention, model access control, review board.",
                "cost":300_000,
                "effects":[{"type":"sentiment","value":4},{"type":"p_adjust","value":0.004,"target":"enterprise"}]
            },
            {
                "label":"Run secure sandbox pilots with Legal oversight",
                "detail":"Build confidence via ring-fenced experiments.",
                "cost":200_000,
                "units":["Finance & Legal","IT & Data Science"],
                "effects":[{"type":"q_adjust","value":0.03,"target":["Finance & Legal","IT & Data Science"]}]
            },
            {
                "label":"Downplay concerns",
                "detail":"Maintain momentum; deal with issues later.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-6}],
                "risks":"Potential compliance incident later."
            },
        ]
    },
    {
        "title":"Data Quality Roadblock",
        "description":"Teams report messy data hampering model performance.",
        "options":[
            {
                "label":"Invest in data cleanup & MDM",
                "detail":"Data catalog, lineage, stewardship roles.",
                "cost":1_500_000,
                "effects":[{"type":"p_adjust","value":0.006,"target":"enterprise"}]
            },
            {
                "label":"Local quick fixes per unit",
                "detail":"Tactical workarounds to keep demos alive.",
                "cost":400_000,
                "effects":[{"type":"q_adjust","value":0.02,"target":"enterprise"}],
                "risks":"Tech debt may slow later scale."
            },
            {
                "label":"Ignore for now",
                "detail":"Hope the vendor models are robust enough.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-4}],
                "risks":"Model failures likely."
            },
        ]
    },
    {
        "title":"Shadow IT Tools Appear",
        "description":"Employees adopt unapproved AI apps to speed up work.",
        "options":[
            {
                "label":"Offer approved alternatives quickly",
                "detail":"Provide sanctioned tools with SSO, logging, and support.",
                "cost":600_000,
                "effects":[{"type":"q_adjust","value":0.03,"target":"enterprise"},{"type":"sentiment","value":3}]
            },
            {
                "label":"Crack down with strict blocks",
                "detail":"Block unapproved tools at the firewall.",
                "cost":100_000,
                "effects":[{"type":"sentiment","value":-6}],
                "risks":"Users find workarounds; morale dips."
            },
            {
                "label":"Tolerate for now",
                "detail":"Monitor the situation without action.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-2}]
            },
        ]
    },
    {
        "title":"Success Story in Operations",
        "description":"A pilot in Operations cuts defect rates by 8%. Word spreads.",
        "options":[
            {
                "label":"Amplify the story enterprise-wide",
                "detail":"Short video, intranet post, Q&A with pilot team.",
                "cost":80_000,
                "effects":[{"type":"q_adjust","value":0.03,"target":"enterprise"},{"type":"adoption_boost","value":4,"target":["Operations"]}]
            },
            {
                "label":"Scale the pilot",
                "detail":"Extend to additional plants with standard playbook.",
                "cost":900_000,
                "units":["Operations"],
                "effects":[{"type":"adoption_boost","value":10,"target":["Operations"]},{"type":"p_adjust","value":0.006,"target":["Operations"]}]
            },
            {
                "label":"Keep it local",
                "detail":"Don’t distract other units.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-1}]
            },
        ]
    },
    {
        "title":"Union Questions Job Security",
        "description":"Labor reps demand guarantees about AI’s impact on staffing.",
        "options":[
            {
                "label":"Formal job transition framework",
                "detail":"No involuntary layoffs; reskilling & redeployment first.",
                "cost":1_200_000,
                "effects":[{"type":"sentiment","value":8},{"type":"q_adjust","value":0.02,"target":"enterprise"}]
            },
            {
                "label":"Limited guarantees, performance focus",
                "detail":"Tie commitments to productivity targets.",
                "cost":400_000,
                "effects":[{"type":"sentiment","value":2},{"type":"p_adjust","value":0.003,"target":"enterprise"}]
            },
            {
                "label":"Decline guarantees",
                "detail":"Maintain flexibility for restructuring.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-8}],
                "risks":"Strikes or slowdowns possible."
            },
        ]
    },
    {
        "title":"Regulator Issues Guidance",
        "description":"New rules clarify AI transparency and auditability requirements.",
        "options":[
            {
                "label":"Comply proactively and certify",
                "detail":"Externally validate controls; train risk owners.",
                "cost":700_000,
                "effects":[{"type":"sentiment","value":4},{"type":"p_adjust","value":0.004,"target":"enterprise"}]
            },
            {
                "label":"Minimal compliance",
                "detail":"Do the basics to avoid fines.",
                "cost":250_000,
                "effects":[{"type":"sentiment","value":1}]
            },
            {
                "label":"Delay action",
                "detail":"Wait for more clarity.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-4}],
                "risks":"Investigations later."
            },
        ]
    },
    {
        "title":"Vendor Negotiation",
        "description":"Major AI vendor offers discount for enterprise license.",
        "options":[
            {
                "label":"Negotiate aggressively for savings",
                "detail":"Consolidate tools; cut redundant spend.",
                "cost":100_000,
                "effects":[{"type":"budget","value":500_000},{"type":"p_adjust","value":0.003,"target":"enterprise"}]
            },
            {
                "label":"Accept offer quickly",
                "detail":"Lock in pricing; focus on rollout.",
                "cost":0,
                "effects":[{"type":"q_adjust","value":0.02,"target":"enterprise"}]
            },
            {
                "label":"Decline and go open-source",
                "detail":"Build internal capability instead of license.",
                "cost":400_000,
                "effects":[{"type":"sentiment","value":-2},{"type":"p_adjust","value":0.004,"target":"enterprise"}],
                "risks":"Delays possible."
            },
        ]
    },
    {
        "title":"Executive Fatigue",
        "description":"Leaders worry AI is distracting from core results.",
        "options":[
            {
                "label":"Refocus on business KPIs",
                "detail":"Tie every AI initiative to revenue, cost, risk KPIs.",
                "cost":200_000,
                "effects":[{"type":"sentiment","value":3},{"type":"q_adjust","value":0.02,"target":"enterprise"}]
            },
            {
                "label":"Reduce scope to top 3 use cases",
                "detail":"Kill or pause low-value pilots.",
                "cost":0,
                "effects":[{"type":"p_adjust","value":0.002,"target":"enterprise"}]
            },
            {
                "label":"Press on with all projects",
                "detail":"Maintain momentum despite concerns.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-3}]
            },
        ]
    },
    {
        "title":"Talent Competition",
        "description":"Rivals poach your top data scientists.",
        "options":[
            {
                "label":"Retention packages + career paths",
                "detail":"Clear progression, recognition, and rewards.",
                "cost":1_000_000,
                "effects":[{"type":"sentiment","value":4},{"type":"p_adjust","value":0.003,"target":"enterprise"}]
            },
            {
                "label":"Upskill internal staff (citizen devs)",
                "detail":"Train power users with guardrails.",
                "cost":500_000,
                "effects":[{"type":"q_adjust","value":0.03,"target":"enterprise"}]
            },
            {
                "label":"Do nothing",
                "detail":"Assume bench is deep enough.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-4}],
                "risks":"Delivery delays."
            },
        ]
    },
    {
        "title":"Showcase & Scale",
        "description":"Board review approaches. Time to prove impact and scale what works.",
        "options":[
            {
                "label":"Enterprise showcase + playbooks",
                "detail":"Publish repeatable patterns; scale the winners.",
                "cost":600_000,
                "effects":[{"type":"q_adjust","value":0.04,"target":"enterprise"},{"type":"sentiment","value":4}]
            },
            {
                "label":"Double down on top 2 units",
                "detail":"Maximize success where traction is highest.",
                "cost":800_000,
                "units":["Pick top units dynamically"],
                "effects":[{"type":"adoption_boost","value":8,"target":"enterprise"}]
            },
            {
                "label":"Quietly close the program",
                "detail":"Claim learnings, pause further investment.",
                "cost":0,
                "effects":[{"type":"sentiment","value":-10}],
                "risks":"Reputation hit; future blockers."
            },
        ]
    },
]
