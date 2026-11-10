---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.13 FinancialInstrumentDetails <FinInstrmDtls>", "30.4.7.13.1 Identification <Id>", "30.4.7.13.1.16 OtherProprietaryIdentification <OthrPrtryId>", "30.4.7.13.1.16.1 Identification <Id>"]
file_pages: [720]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.13.1.16.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 720 to 720.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 720

```text
OtherProprietaryIdentification <OthrPrtryId> contains the following
AlternateSecurityIdentification7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 720
   IdentificationSource <IdSrc> [1..1] ± 720
30.4.7.13.1.16.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a security.
Datatype: "Max35Text" on page 5403
30.4.7.13.1.16.2  IdentificationSource <IdSrc>
Presence: [1..1]
Definition: Source of the identification, that is, domestic (national) or proprietary.
IdentificationSource <IdSrc> contains one of the following elements (see
"IdentificationSource1Choice" on page 4550 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Domestic <Dmst> [1..1] CodeSet C12 4550
Or}   Proprietary <Prtry> [1..1] Text 4551
30.4.7.13.2  Name <Nm>
Presence: [0..1]
Definition: Name of the financial instrument in free format text.
Datatype: "Max350Text" on page 5403
30.4.7.13.3  ShortName <ShrtNm>
Presence: [0..1]
Definition: Financial Instrument Short Name (FISN) expressed in conformance with the ISO 18774
standard.
Datatype: "Max35Text" on page 5403
30.4.7.13.4  SupplementaryIdentification <SplmtryId>
Presence: [0..1]
Definition: Additional information about the financial instrument.
Datatype: "Max35Text" on page 5403
30.4.7.13.5  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. For example, a unit may have a specific load structure,
for example, front end or back end, an income policy, for example, pay out or accumulate, or a trailer
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 720 May 2026
```

