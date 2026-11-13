---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["2 semt.028.001.01 IntraPositionMovementQueryV01", "2.4 Message Building Blocks", "2.4.1 QueryDefinition <QryDef>", "2.4.1.2 SearchCriteria <SchCrit>", "2.4.1.2.5 SafekeepingAccount <SfkpgAcct>"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 2.4.1.2.5 SafekeepingAccount <SfkpgAcct>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
SafekeepingAccountOwner <SfkpgAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 257
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 257
2.4.1.2.5  SafekeepingAccount <SfkpgAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 193 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 193
   Type <Tp> [0..1] ± 193
   Name <Nm> [0..1] Text 193
2.4.1.2.6  BalanceType <BalTp>
Presence: [0..*]
Definition: Balance to which the amount of money is moved.
Impacted by: C3 "BalanceFromToRule"
BalanceType <BalTp> contains the following IntraPositionType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [0..1] ± 30
   BalanceTo <BalTo> [0..1] ± 31
Constraints
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
2.4.1.2.6.1  BalanceFrom <BalFr>
Presence: [0..1]
Definition: Balance from which the securities are moving.
Approved by the Securities SEG on 21 August 2025 semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities - Settlement Restrictions 30 September 2025
```

