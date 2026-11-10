---
template: false
document_kind: "source-limitation"
manual_curated: true
review_status: "needs-review"
title: "Securities reporting source-example limitations"
domain: "securities"
source_ids: ["src-000374"]
source_locations: [{"source_id": "src-000374", "locator": "P147 Word11; P424-P541 Word31-34; P1052/P1053 Word48; P1703 Word66; P1858 Word70"}]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.027.001.01", "semt.044.001.01"]
issue_ids: ["issue-000057"]
limitations: ["Original penalty XML has duplicate opening root and one closing root.", "INST example contains status/reason despite the explicit business usage prohibition.", "Penalty matched timestamp22025 conflicts with surrounding2025 chronology."]
source_editions: ["march-2026"]
---

# Securities reporting source-example limitations

[src-000374](../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; original examples preserved without repair.

| Source locator | Source evidence and implication |
| --- | --- |
| P1052/P1053 Word48; P1858 Word70 | Two SctiesTxPnltiesRpt opening tags and one closing tag make the original daily-penalty example not well-formed XML. No corrected payload is silently substituted. |
| P147 Word11 versus P424-P541 Word31-34 | INST usage says Transactions/StatusAndReason must not be present, but the instruction-response example has QryTp INST and StsAndRsn with matched/settled content. Its structure passes the exact XSD after a documented envelope; the business condition remains violated. |
| P1703 Word66 | Literal MtchdStsTmStmp22025-06-21T14:30:15Z is retained beside acknowledgment and business dates in2025. The intended timestamp is unresolved. |



Eight other payloads parse as XML and pass the supplied exact schema after adding only the exact namespace and Document envelope. This derived check does not rewrite the original fragment or resolve business-rule contradictions. All nine original payloads have independent paragraph-text corroboration against the Word PDF with zero unmatched paragraphs.
