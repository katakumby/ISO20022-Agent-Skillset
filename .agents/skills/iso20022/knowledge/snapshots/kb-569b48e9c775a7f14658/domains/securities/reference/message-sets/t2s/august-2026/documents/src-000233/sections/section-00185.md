---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["14 camt.076.001.01 BillingReportRequestV01", "14.4 Message Building Blocks", "14.4.2 SearchCriteria <SchCrit>", "14.4.2.6 AccountIdentification <AcctId>"]
file_pages: [238, 239]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.076.001.01"]
---

# 14.4.2.6 AccountIdentification <AcctId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 238 to 239.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 238

```text
PartyIdentification <PtyId> contains the following elements (see "PartyIdentification136" on page 3060
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3060
   LEI <LEI> [0..1] IdentifierSet 3060
14.4.2.6  AccountIdentification <AcctId>
Presence: [0..1]
Definition: Either securities account or dedicated cash account number.
AccountIdentification <AcctId> contains one of the following AccountIdentification38Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 238
Or}   CashAccountIdentification <CshAcctId> [1..1] ± 238
14.4.2.6.1  SecuritiesAccountIdentification <SctiesAcctId>
Presence: [1..1]
Definition: Unique identification of the securities account as assigned by the account servicer.
SecuritiesAccountIdentification <SctiesAcctId> contains the following elements (see
"SecuritiesAccount19" on page 2834 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2834
   Type <Tp> [0..1] ± 2834
   Name <Nm> [0..1] Text 2834
14.4.2.6.2  CashAccountIdentification <CshAcctId>
Presence: [1..1]
Definition: Unique identification of the cash account, as assigned by the account servicer.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
14.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 238 August 2026
```

## File page 239

```text
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C5 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.076.001.01 BillingReportRequestV01
Target2-Securities 239 August 2026
```

