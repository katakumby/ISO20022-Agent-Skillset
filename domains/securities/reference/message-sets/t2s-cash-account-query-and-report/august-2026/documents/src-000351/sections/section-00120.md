---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.2 Account Identification", "7.1.2.1 AccountIdentification4Choice", "7.1.2.1.2 Other <Othr>"]
file_pages: [135]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.2.1.2 Other <Othr>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 135 to 135.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 135

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
7.1.2.1.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 133 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 133
   SchemeName <SchmeNm> [0..1]  133
{Or     Code <Cd> [1..1] CodeSet 134
Or}     Proprietary <Prtry> [1..1] Text 134
   Issuer <Issr> [0..1] Text 134
7.1.3 Bank Transaction Code
7.1.3.1  BankTransactionCodeStructure4
Definition: Set of elements used to identify the type or operations code of a transaction entry.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Domain <Domn> [0..1] ± 136
   Proprietary <Prtry> [0..1]  136
     Code <Cd> [1..1] Text 136
     Issuer <Issr> [0..1] Text 136
Constraints
• DomainOrProprietaryRule
Either Proprietary or Domain or both must be present.
Following Must be True
    /Domain Must be present
 Or    /Proprietary Must be present
• FamilyAndSubFamilyRule
If a specific (non-generic) Family code is not present, then a specific (non-generic) SubFamily code
is not allowed.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 135 August 2026
```

