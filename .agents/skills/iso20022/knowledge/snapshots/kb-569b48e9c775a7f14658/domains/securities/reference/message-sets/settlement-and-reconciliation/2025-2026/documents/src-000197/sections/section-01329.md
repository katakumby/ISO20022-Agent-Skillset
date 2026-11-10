---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.1 SettlementDetails220", "35.1.26.1.28 EligibleForCollateral <ElgblForColl>"]
file_pages: [1791]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.1.28 EligibleForCollateral <ElgblForColl>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1791 to 1791.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1791

```text
ModificationCancellationAllowed <ModCxlAllwd> contains one of the following elements (see
"ModificationCancellationAllowed4Choice" on page 1588 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1588
Or}   Proprietary <Prtry> [1..1] ± 1589
35.1.26.1.28  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.26.1.29  DeliveringSecuritiesSubBalanceType <DlvrgSctiesSubBalTp>
Presence: [0..1]
Definition: Specifies the delivering securities sub balance type indicator (example restriction type for a
market infrastructure).
DeliveringSecuritiesSubBalanceType <DlvrgSctiesSubBalTp> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.26.1.30  ReceivingSecuritiesSubBalanceType <RcvgSctiesSubBalTp>
Presence: [0..1]
Definition: Specifies the receiving securities sub balance type indicator (example restriction type for a
market infrastructure).
ReceivingSecuritiesSubBalanceType <RcvgSctiesSubBalTp> contains the following elements (see
"GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1791 March 2026
```

