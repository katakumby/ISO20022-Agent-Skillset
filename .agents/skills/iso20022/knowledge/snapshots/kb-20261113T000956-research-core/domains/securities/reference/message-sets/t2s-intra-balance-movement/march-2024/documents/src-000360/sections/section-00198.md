---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["11 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "11.4 Message Building Blocks", "11.4.2 QueryDefinition <QryDef>", "11.4.2.2 SearchCriteria <SchCrit>", "11.4.2.2.2 ProcessingStatus <PrcgSts>"]
file_pages: [239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 11.4.2.2.2 ProcessingStatus <PrcgSts>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 239 to 239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 239

```text
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 497
11.4.2.2.2  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ModificationProcessingStatus9Choice" on page 448 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 448
Or}   Proprietary <Prtry> [1..1] ± 449
11.4.2.2.3  CashAccount <CshAcct>
Presence: [0..*]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 239
Or   ContainText <CTTxt> [1..1] Text 239
Or}   NotContainText <NCTTxt> [1..1] Text 239
11.4.2.2.3.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 391
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C9 391
Or}   Other <Othr> [1..1] ± 392
11.4.2.2.3.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 497
11.4.2.2.3.3  NotContainText <NCTTxt>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
239 March 2024
```

