// Users
CREATE (:User {name: "UserA", role: "Employee"});
CREATE (:User {name: "Admin1", role: "Administrator"});

// Machines
CREATE (:Machine {name: "Workstation1", os: "Windows"});
CREATE (:Machine {name: "DBServer", os: "Linux"});

// Services
CREATE (:Service {name: "WebApp"});
CREATE (:Service {name: "DatabaseService"});

// Vulnerabilities
CREATE (:Vulnerability {name: "CVE-2023-9999", severity: "Critical"});

// Relationships
MATCH (u:User {name: "UserA"}), (m:Machine {name: "Workstation1"})
CREATE (u)-[:HAS_ACCESS]->(m);

MATCH (m:Machine {name: "Workstation1"}), (s:Service {name: "WebApp"})
CREATE (m)-[:RUNS]->(s);

MATCH (s:Service {name: "WebApp"}), (db:Machine {name: "DBServer"})
CREATE (s)-[:CONNECTED_TO]->(db);

MATCH (db:Machine {name: "DBServer"}), (v:Vulnerability {name: "CVE-2023-9999"})
CREATE (db)-[:HAS_VULNERABILITY]->(v);