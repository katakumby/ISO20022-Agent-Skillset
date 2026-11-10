---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["13 camt.082.001.02 IntraBalanceMovementCancellationQueryV02", "13.4 Message Building Blocks", "13.4.2 QueryDefinition <QryDef>", "13.4.2.2 SearchCriteria <SchCrit>", "13.4.2.2.3 CashAccount <CshAcct>", "13.4.2.2.3.1 Equal <EQ>"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.082.001.02"]
---

# 13.4.2.2.3.1 Equal <EQ>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
CashAccount <CshAcct> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 295
Or   ContainText <CTTxt> [1..1] Text 295
Or}   NotContainText <NCTTxt> [1..1] Text 295
13.4.2.2.3.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 391
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C9 391
Or}   Other <Othr> [1..1] ± 392
13.4.2.2.3.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 497
13.4.2.2.3.3  NotContainText <NCTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on a pattern that cannot be contained in the account
identification.
Datatype: "Max35Text" on page 497
13.4.2.2.4  CashAccountOwner <CshAcctOwnr>
Presence: [0..*]
Definition: Party that owns the account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 420 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 420
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 420
13.4.2.2.5  CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.082.001.02
IntraBalanceMovementCancellationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
295 March 2024
```

