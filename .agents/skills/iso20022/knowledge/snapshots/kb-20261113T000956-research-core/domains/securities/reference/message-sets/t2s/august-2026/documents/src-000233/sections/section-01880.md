---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["73 semt.028.001.01 IntraPositionMovementQueryV01", "73.4 Message Building Blocks", "73.4.1 QueryDefinition <QryDef>", "73.4.1.2 SearchCriteria <SchCrit>", "73.4.1.2.5 SafekeepingAccount <SfkpgAcct>"]
file_pages: [2585]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.028.001.01"]
---

# 73.4.1.2.5 SafekeepingAccount <SfkpgAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2585 to 2585.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2585

```text
SafekeepingAccountOwner <SfkpgAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
73.4.1.2.5  SafekeepingAccount <SfkpgAcct>
Presence: [0..*]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
73.4.1.2.6  BalanceType <BalTp>
Presence: [0..*]
Definition: Balance to which the amount of money is moved.
Impacted by: C3 "BalanceFromToRule"
BalanceType <BalTp> contains the following IntraPositionType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BalanceFrom <BalFr> [0..1] ± 2585
   BalanceTo <BalTo> [0..1] ± 2586
Constraints
• BalanceFromToRule
The cash balance type of BalanceFrom must be different from the cash balance type of BalanceTo.
73.4.1.2.6.1  BalanceFrom <BalFr>
Presence: [0..1]
Definition: Balance from which the securities are moving.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.028.001.01 IntraPositionMovementQueryV01
Target2-Securities 2585 August 2026
```

