---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.7 Underlying <Undrlyg>", "5.4.3.4.7.1 IntraPositionMovement <IntraPosMvmnt>", "5.4.3.4.7.1.5 BalanceTo <BalTo>"]
file_pages: [128]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.7.1.5 BalanceTo <BalTo>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 128 to 128.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 128

```text
BalanceFrom <BalFr> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 199 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
5.4.3.4.7.1.5  BalanceTo <BalTo>
Presence: [0..1]
Definition: Balance to which the securities are moving.
BalanceTo <BalTo> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 199 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
5.4.3.4.7.1.6  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..1]
Definition: Number identifying a lot constituting the sub-balance.
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 225 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 226
   Issuer <Issr> [0..1] Text 226
5.4.3.4.7.1.7  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 230 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 230
Or}   Proprietary <Prtry> [1..1] ± 230
5.4.3.4.7.2  SettlementTransaction <SttlmTx>
Presence: [1..1]
Definition: Specifies the requested settlement transaction details.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 128 September 2025
```

