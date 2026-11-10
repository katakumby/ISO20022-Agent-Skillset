---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["BusinessProcess Description", "Report Query Request"]
content_origin: "source-transcription"
---

# Report Query Request

Source: [src-000343](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Locator: heading path BusinessProcess Description / Report Query Request.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P111** Report Query Request

**P112** The following diagram gives an overview of different types of queries used within Central System:

**P113** Settlement Instruction Queries: 

**P114** Central System shall allow Central System Actors to perform queries on settlement instructions based on the actor’s roles and privileges. For example, for System Actors all instructions that have been sent by either the  System Actor or by other Central System Actors that have been authorised by the System Actor to do so;

**P115** Securities Account Position Queries:

**P116** System users of CSD Participants, CSDs as well as payment banks and NCBs are allowed to send Securities Account Position and Securities Account Position History Queries.

**P117** Cash Related Queries: 

**P118** Central System shall provide NCBs, settlement banks and payment banks, in accordance with their access rights, with the possibility to query e. g. the current balance of one or more Central System dedicated cash accounts.

**P119** Dynamic Data Queries: 

**P120** The only query in this section is the “Report Query”, which provides a System user with the possibility to query the latest available report.

**P121** Static Data Queries:

**P122** Central System shall provide static data queries to all directly connected System actors. A System Actor shall be able to perform only those queries for which the actor has the necessary privileges. The queries shall return only those data for which the System actor has the necessary access right.

[fig-0002 - original figure evidence](../diagrams/fig-0002.md)

**P124**   


**P126** Report query process

[T8 - complete table](../tables/tbl-0008.md)

**P128**   


