---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["18 camt.080.001.02 IntraBalanceMovementModificationQueryV02", "18.4 Message Building Blocks", "18.4.2 QueryDefinition <QryDef>", "18.4.2.2 SearchCriteria <SchCrit>", "18.4.2.2.2 ProcessingStatus <PrcgSts>"]
file_pages: [430]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.080.001.02"]
---

# 18.4.2.2.2 ProcessingStatus <PrcgSts>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 430 to 430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

```text
Definition: Collective reference identifying a set of messages.
Datatype: "Max35Text" on page 3328
18.4.2.2.2  ProcessingStatus <PrcgSts>
Presence: [0..*]
Definition: Provides the status of settlement of a transaction.
ProcessingStatus <PrcgSts> contains one of the following elements (see
"ModificationProcessingStatus9Choice" on page 3175 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3175
Or}   Proprietary <Prtry> [1..1] ± 3175
18.4.2.2.3  CashAccount <CshAcct>
Presence: [0..*]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 430
Or   ContainText <CTTxt> [1..1] Text 430
Or}   NotContainText <NCTTxt> [1..1] Text 430
18.4.2.2.3.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 2836
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
18.4.2.2.3.2  ContainText <CTTxt>
Presence: [1..1]
Definition: Search for one or more accounts based on partial identification of the account(s).
Datatype: "Max35Text" on page 3328
18.4.2.2.3.3  NotContainText <NCTTxt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.080.001.02
IntraBalanceMovementModificationQueryV02
Target2-Securities 430 August 2026
```

