---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "11.4 Message Building Blocks", "11.4.2 QueryDefinition <QryDef>", "11.4.2.2 SearchCriteria <SchCrit>", "11.4.2.2.4 CashAccountOwner <CshAcctOwnr>"]
file_pages: [240]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 11.4.2.2.4 CashAccountOwner <CshAcctOwnr>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 240 to 240.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 240

```text
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 497
11.4.2.2.4  CashAccountOwner <CshAcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 420
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 420
11.4.2.2.5  CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
CashAccountServicer <CshAcctSvcr> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 400 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  401
     BICFI <BICFI> [0..1] IdentifierSet C6 401
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 402
     LEI <LEI> [0..1] IdentifierSet 402
     Name <Nm> [0..1] Text 402
     PostalAddress <PstlAdr> [0..1] ± 402
     Other <Othr> [0..1] ± 403
   BranchIdentification <BrnchId> [0..1]  404
     Identification <Id> [0..1] Text 404
     LEI <LEI> [0..1] IdentifierSet 404
     Name <Nm> [0..1] Text 404
     PostalAddress <PstlAdr> [0..1] ± 404
11.4.2.2.6  MessageOriginator <MsgOrgtr>
Presence: [0..*]
Definition: Party that originated the message, if other than the sender.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
240 March 2024
```

