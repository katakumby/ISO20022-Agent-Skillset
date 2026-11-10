---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["2 acmt.025.001.02 AccountQueryListV02", "2.4 Message Building Blocks", "2.4.5 AccountSearchCriteria <AcctSchCrit>", "2.4.5.24 ReferenceAccountIdentification <RefAcctId>"]
file_pages: [38]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.025.001.02"]
---

# 2.4.5.24 ReferenceAccountIdentification <RefAcctId>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 38 to 38.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 38

```text
2.4.5.24  ReferenceAccountIdentification <RefAcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification of the account used as a reference for the opening of
another account.
ReferenceAccountIdentification <RefAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 134 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C11 134
Or}   Other <Othr> [1..1] ± 135
2.4.5.25  Proprietary <Prtry>
Presence: [0..*]
Definition: Proprietary characteristics of the account.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 145 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 146
   SchemeName <SchmeNm> [0..1] Text 146
   Issuer <Issr> [0..1] Text 146
2.4.5.26  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following OrganisationIdentification39 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C2 39
   LEI <LEI> [0..1] IdentifierSet 39
   Other <Othr> [0..*]  39
     Identification <Id> [1..1] Text 39
     SchemeName <SchmeNm> [0..1]  39
{Or       Code <Cd> [1..1] CodeSet 40
Or}       Proprietary <Prtry> [1..1] Text 40
     Issuer <Issr> [0..1] Text 40
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.025.001.02 AccountQueryListV02
Target2-Securities - Cash Account Query and Report 38 August 2026
```

