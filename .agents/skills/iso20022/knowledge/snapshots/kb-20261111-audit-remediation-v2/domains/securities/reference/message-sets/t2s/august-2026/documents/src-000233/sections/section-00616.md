---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.47 ContactName <CtctNm>", "27.4.2.3.47.2 Identification <Id>", "27.4.2.3.47.2.1 AnyBIC <AnyBIC>"]
file_pages: [801]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.47.2.1 AnyBIC <AnyBIC>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 801 to 801.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 801

```text
Identification <Id> contains one of the following PartyIdentification177Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C3 801
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 801
27.4.2.3.47.2.1  AnyBIC <AnyBIC>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C3 "AnyBIC"
Datatype: "AnyBICDec2014Identifier" on page 3320
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
27.4.2.3.47.2.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
27.4.2.3.47.3  Purpose <Purp>
Presence: [0..1]
Definition: Purpose of the organisation, eg, charity.
Datatype: "Max35Text" on page 3328
27.4.2.3.47.4  TaxationCountry <TaxtnCtry>
Presence: [0..1]
Definition: Country of taxation of an organisation.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 3234
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 801 August 2026
```

