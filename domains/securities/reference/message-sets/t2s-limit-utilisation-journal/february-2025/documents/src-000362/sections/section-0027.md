---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["Business Examples", "Example #2: Operational Errors", "Description"]
content_origin: "source-transcription"
---

# Description

Source: [src-000362](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Locator: heading path Business Examples / Example #2: Operational Errors / Description.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P313** Description

**P314** In this example the “LimitUtilisationJournalQuery” is used by an NCB (H) "CBHHBIC2XXX”, participating in T2S, to query via camt.064 the journal utilisation of Auto-collateralisation limits for the payment bank “PBKHBIC0XXX” on January 9th, 2015 with Limit Utilisation activity date in the future.

**P315** The result of this query is sent using “LimitUtilisationJournalReport” (camt.065) specifying the operational error resulting from the processing of this request.

**P316** In this example, the Error Code “Q065” is returned with the corresponding Error description.

