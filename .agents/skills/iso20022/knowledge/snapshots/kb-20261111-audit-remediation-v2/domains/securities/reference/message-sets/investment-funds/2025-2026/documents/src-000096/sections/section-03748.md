---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.40 CRSForm1Choice", "66.1.30.40.1 Code <Cd>"]
file_pages: [5034]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.40.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5034 to 5034.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5034

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5034
Or}   Proprietary <Prtry> [1..1] ± 5034
66.1.30.40.1  Code <Cd>
Presence: [1..1]
Definition: Type of Foreign Account Tax Compliance Act (FATCA) form expressed as a code.
Datatype: "CRSFormType1Code" on page 5291
CodeName Name Definition
CER4 CertificateIdentificationGovernment Certificate of Identification issued by a
government.
CER3 CertificateOfResidence Certificate of residence.
CER5 OfficialDocumentGovernmentForEntity Official documentation issued by a
government for the entity.
CER6 OtherDocumentOrReport Financial statement, third party credit
report, bankruptcy filing or a securities
regulator report.
CER8 PublicInformationEntity Publicly available information for the
entity.
CER1 SelfCertificationSeparateDocument Self certification as a separate
document.
CER2 SelfCertificationWithAccountOpeningContract Self certification as a document included
into contract of the account opening.
CER7 Standardised Standardised industry coding system for
the entity.
66.1.30.40.2  Proprietary <Prtry>
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
66.1.30.41  CRSStatus4
Definition: Common Reporting Standard (CRS) status information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5034 May 2026
```

