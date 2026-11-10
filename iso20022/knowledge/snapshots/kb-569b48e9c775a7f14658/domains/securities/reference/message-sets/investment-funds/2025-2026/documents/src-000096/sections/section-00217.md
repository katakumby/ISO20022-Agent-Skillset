---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.12 Issuer <Issr>"]
file_pages: [317]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.12 Issuer <Issr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 317 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 317

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
15.4.5.8.12  Issuer <Issr>
Presence: [0..1]
Definition: Issuer of the financial instrument. When used in reference to MiFID, this is in the scope of the
European MiFID Template (EMT) reference 00070.
Issuer <Issr> contains the following elements (see "ContactAttributes5" on page 5021 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5021
   PostalAddress <PstlAdr> [0..1] ± 5021
   PhoneNumber <PhneNb> [0..1] Text 5022
   FaxNumber <FaxNb> [0..1] Text 5022
   EmailAddress <EmailAdr> [0..1] Text 5022
   URLAddress <URLAdr> [0..1] Text 5022
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5022
   LEI <LEI> [0..1] IdentifierSet 5023
15.4.5.8.13  IssuerProductGovernanceProcess <IssrPdctGovncPrc>
Presence: [0..1]
Definition: Governance procedure that must be followed. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 00075.
IssuerProductGovernanceProcess <IssrPdctGovncPrc> contains one of the following elements
(see "GovernanceProcess1Choice" on page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4508
Or}   Proprietary <Prtry> [1..1] ± 4509
15.4.5.8.14  ProductCategory <PdctCtgy>
Presence: [0..1]
Definition: Designation of the product category or nature, for example, Pacific Equity, Equity Fund,
Money Market Fund. If the product is a structured security product, the European Structured Investment
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 317 May 2026
```

