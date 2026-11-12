---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.6 BalanceType <BalTp>", "2.4.1.2.6.2 BalanceTo <BalTo>"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.6.2 BalanceTo <BalTo>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
BalanceFrom <BalFr> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 199 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
2.4.1.2.6.2  BalanceTo <BalTo>
Presence: [0..1]
Definition: Balance to which the securities are moving.
BalanceTo <BalTo> contains the following elements (see
"SecuritiesSubBalanceTypeAndQuantityBreakdown3" on page 199 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 200
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 200
2.4.1.2.7  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..*]
Definition: Number identifying a lot constituting the sub-balance.
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 225 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 226
   Issuer <Issr> [0..1] Text 226
2.4.1.2.8  SettlementQuantity <SttlmQty>
Presence: [0..1]
Definition: Total quantity of securities to be settled.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 31 September 2025
```

