---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["Business Examples", "Example #1: Business Report", "Description"]
content_origin: "source-transcription"
---

# Description

Source: [src-000362](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Locator: heading path Business Examples / Example #1: Business Report / Description.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P168** Description

**P169** In this example the “LimitUtilisationJournalQuery” is used by an NCB (A) "CBAABIC1XXX”, participating in T2S, to query via camt.064 the journal utilisation of Auto-collateralisation limits for the payment bank “PAYBKBICXXX” on January 9th, 2015, as the current business date, which corresponds to Limit Utilisation activity date.

**P170** The result of this query is sent using “LimitUtilisationJournalReport” (camt.065) containing the Auto-collateralisation limit, associated limit information and corresponding journal transaction activity of the utilisation of the limit for the bank linked to the Dedicated Cash Account identified by “9000000123”. 

**P171** In this example, the following limit information is returned:

**P172** Limit Amount: 100000 Euros;

**P173** Utilisation: 40000 Euros;

**P174** Available: 60000 Euros;

**P175** Journal Activity :

**P176** 15000 Euros Debit for Entry Reference T2SREF1234

**P177** 12000 Euros Debit for Entry Reference T2SREF2345

**P178** 13000 Euros Debit for Entry Reference T2SREF3456

