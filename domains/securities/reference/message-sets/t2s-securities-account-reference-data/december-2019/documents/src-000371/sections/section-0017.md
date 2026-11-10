---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Scope and Functionality", "Groups of MessageDefinitions and Functionality", "Functionality", "Securities Account Query (reda.019)"]
content_origin: "source-transcription"
---

# Securities Account Query (reda.019)

Source: [src-000371](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Scope and Functionality / Groups of MessageDefinitions and Functionality / Functionality / Securities Account Query (reda.019).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P103** Securities Account Query (reda.019)

**P104** Securities Account Query (reda.019) is sent by an authorised party to query on securities account reference data.  

**P105** This message is sent to the servicing party to make the following type of queries:

**P106** Securities Account Reference Data Query;

**P107** Securities Account List Query.

**P108** Depending on the query criteria, it is possible that the processing will take more than a certain time or that the query will not retrieve any record. In this case, an error is sent to the Instructing Party within the Securities Account Report (reda.021);

**P109** Search criteria include the following elements: 

**P110** Account identification;

**P111** Account servicer;

**P112** Account owner;

**P113** Responsible party type;

**P114** Opening and closing date;

**P115** Account type;

**P116** End investor flag; 

**P117** Pricing scheme.

