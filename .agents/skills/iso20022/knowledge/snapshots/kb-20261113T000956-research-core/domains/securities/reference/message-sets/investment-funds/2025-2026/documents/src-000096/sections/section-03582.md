---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.14 FATCAForm1Choice", "66.1.28.14.1 Code <Cd>"]
file_pages: [4832]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.14.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4832 to 4832.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4832

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4832
Or}   Proprietary <Prtry> [1..1] ± 4832
66.1.28.14.1  Code <Cd>
Presence: [1..1]
Definition: Type of Foreign Account Tax Compliance Act (FATCA) form expressed as a code.
Datatype: "FATCAFormType1Code" on page 5300
CodeName Name Definition
CER5 CertificateForeignIntermediary Certificate of foreign intermediary (also
known as IRS form W-8IMY).
CER7 CertificateForeignPersonsClaim Certificate of foreign person's claim that
income is effectively connected with the
conduct of a trade or business in the
United States (also known as IRS form
W-8BEN-E).
CER1 CertificateForeignStatusBeneficialOwner Certificate of foreign status of beneficial
owner (also known as IRS form
W-8BEN).
CER2 CertificateLossNationality Certificate of loss of nationality.
CER3 SelfCertification Self certification.
CER4 SelfCertificationLossNationality Self certificate of loss of nationality (also
known as IRS form I-407).
CER6 TaxpayerIdentificationNumberRequest Form is a request for taxpayer
identification number and certification
(also known as IRS form W9).
66.1.28.14.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of Foreign Account Tax Compliance Act (FATCA) form expressed as a proprietary
code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.15  LevelOfControl1Choice
Definition: Choice of formats for the level of control.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4832 May 2026
```

