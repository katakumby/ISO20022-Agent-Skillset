---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.7 Underlying <Undrlyg>", "76.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>", "76.4.3.4.7.1.5 BalanceTo <BalTo>"]
file_pages: [2683]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.7.1.5 BalanceTo <BalTo>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2683 to 2683.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2683

```text
BalanceFrom <BalFr> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 2854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 2854
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2854
76.4.3.4.7.1.5  BalanceTo <BalTo>
Presence: [0..1]
Definition: Balance to which the securities are moving.
BalanceTo <BalTo> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 2854 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 2854
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2854
76.4.3.4.7.1.6  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 2965 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
76.4.3.4.7.1.7  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 2981 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
76.4.3.4.7.2  SettlementTransaction <SttlmTx>
Presence: [1..1]
Definition: Specifies the requested settlement transaction details.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2683 August 2026
```

