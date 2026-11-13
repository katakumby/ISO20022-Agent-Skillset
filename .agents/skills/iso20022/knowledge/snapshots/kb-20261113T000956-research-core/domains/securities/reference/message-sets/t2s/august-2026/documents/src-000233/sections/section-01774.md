---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.8 SafekeepingAccount <SfkpgAcct>"]
file_pages: [2437]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.8 SafekeepingAccount <SfkpgAcct>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2437 to 2437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2437

```text
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 2981 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
71.4.1.2.8  SafekeepingAccount <SfkpgAcct>
Presence: [0..*]
Definition: Account where financial instruments are maintained.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
71.4.1.2.9  CashAccount <CshAcct>
Presence: [0..*]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 2437
Or   ContainText <CTTxt> [1..1] Text 2438
Or}   NotContainText <NCTTxt> [1..1] Text 2438
71.4.1.2.9.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 2836
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2437 August 2026
```

