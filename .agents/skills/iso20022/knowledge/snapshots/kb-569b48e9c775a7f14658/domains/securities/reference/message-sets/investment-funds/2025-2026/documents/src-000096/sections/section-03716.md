---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.20 FundParties1"]
file_pages: [5001]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.20 FundParties1

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5001 to 5001.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5001

```text
RegisteredShareholderName <RegdShrhldrNm> contains one of the following elements (see
"RegisteredShareholderName1Choice" on page 4917 for details)
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
66.1.30.20  FundParties1
Definition: Parties related to an investment fund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Guarantor <Guarntr> [0..1] ± 5001
   Auditor <Audtr> [0..1] ± 5002
   Trustee <Trstee> [0..1] ± 5002
   OtherParty <OthrPty> [0..*] ± 5003
66.1.30.20.1  Guarantor <Guarntr>
Presence: [0..1]
Definition: Guarantor of the financial instrument. When used in reference to MiFID, this is in the scope
of the European MiFID Template (EMT) reference 00080.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5001 May 2026
```

