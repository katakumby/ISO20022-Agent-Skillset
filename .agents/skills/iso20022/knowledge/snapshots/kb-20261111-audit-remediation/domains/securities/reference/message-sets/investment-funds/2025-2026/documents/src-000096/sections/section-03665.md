---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.6 CompanyLink1Choice", "66.1.30.6.2 Proprietary <Prtry>"]
file_pages: [4917]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.6.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4917 to 4917.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4917

```text
CodeName Name Definition
PCOM ParentCompany Parent company of the broker.
RELA Relative Spouse or partner and child of an
employee, operator or agent of the
broker; agent of the broker; brokerage
partners or shareholders; individual or
entity who holds a direct or an indirect
control function and the holder of a
management or an administration
position.
66.1.30.6.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Company link expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.7  RegisteredShareholderName1Choice
Definition: Choice of individual or organisation name and address.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndividualPerson <IndvPrsn> [1..1]  4918
     NamePrefix <NmPrfx> [0..1]  4918
{Or       Code <Cd> [1..1] CodeSet 4918
Or}       Proprietary <Prtry> [1..1] ± 4918
     GivenName <GvnNm> [0..1] Text 4919
     MiddleName <MddlNm> [0..1] Text 4919
     Name <Nm> [1..1] Text 4919
     PostalAddress <PstlAdr> [1..5] ± C23 4919
Or}   Organisation <Org> [1..1]  4920
     Name <Nm> [1..1] Text 4921
     ShortName <ShrtNm> [0..1] Text 4921
     PostalAddress <PstlAdr> [1..5] ± C23 4921
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4917 May 2026
```

