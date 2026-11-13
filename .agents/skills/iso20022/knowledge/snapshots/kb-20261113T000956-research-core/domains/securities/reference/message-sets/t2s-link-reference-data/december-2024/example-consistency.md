---
template: false
document_kind: "source-limitation"
manual_curated: true
review_status: "needs-review"
title: "Link source example consistency"
domain: "securities"
source_ids: ["src-000365"]
message_sets: ["t2s-link-reference-data"]
message_ids: ["reda.045.001.01", "reda.047.001.01", "reda.049.001.01", "reda.051.001.01"]
source_locations: [{"source_id": "src-000365", "locator": "P246/P320/P327/P338/P365–404; Word23/25–28; P414/P419/P437/P478/P484/P495–497; Word28–32"}]
issue_ids: ["issue-000053"]
limitations: ["Supplied examples contain conflicting correlation IDs, issuer/investor role labels and a cash-settlement boolean; preserve each payload independently."]
source_editions: ["december-2024"]
---

# Source example consistency

[src-000365](../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_LinkReferenceData_v2.docx`; all ten examples are retained independently and visually compared. They are not certified as a consistent request/response chain.

| Source evidence | Unresolved source claims |
| --- | --- |
| Security creation P246/Word23 versus status introduction P320/Word25 | Creation MsgId SECCSDLINKREQ and IssrCSD; status introduction says it relates to the creation. |
| Completed narrative P327/Word25 versus payload P338/Word26 | Narrative RequestMessageID SECCSDINVLINKREQ and InvestorCSD; payload OrgnlBizInstr/Id has surrounding spaces around SECCSDLINCRE and uses InvstrCSD. Neither ID equals creation SECCSDLINKREQ. |
| Queued/rejected P365–404/Word27–28 | Narrative and status payloads use SECCSDLINCRE, again unmatched to supplied creation SECCSDLINKREQ. |
| Account creation P419/Word28 versus statuses P484/P495–497/Word30 | Creation MsgId CREACCLINK; statuses reference ACCLINKCREAT. |
| Account creation P414/Word28 versus payload P437/Word29 | Narrative Cash Settlement Indicator is false; literal CshSttlmInd in XML is true. Both are preserved. |
| Account status introduction P478/Word30 | Source refers to chapter7.4; the supplied account creation appears under7.1.4. |



Issue [issue-000053](../../../../../../tracking/issues.md) remains open. The XML fragments are well-formed; namespace/document-wrapper omissions prevent a standalone XSD-validity claim.
