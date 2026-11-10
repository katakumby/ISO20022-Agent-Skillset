---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.46 FinancialInstrumentForm <FinInstrmForm>", "13.1.6.4.46.1 BookingAppearance <BookgApprnc>", "13.1.6.4.46.1.1 Code <Cd>"]
file_pages: [449]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.46.1.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 449 to 449.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 449

```text
BookingAppearance <BookgApprnc> contains one of the following Appearance3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 449
Or}   Proprietary <Prtry> [1..1] ± 449
13.1.6.4.46.1.1  Code <Cd>
Presence: [1..1]
Definition: Appearance expressed as an ISO 20022 code.
Datatype: "Appearance1Code" on page 509
CodeName Name Definition
DELI Deliverable Physical certificates exist.
NDEL NotDeliverable Not yet deliverable contract.
LIMI Limited Limited or partial deliverability.
BENT BookEntry Security exists only as an electronic
record, ie, there are no physical
certificates representing the security.
DFBE DeferredBookEntry Deferred printing, book entry.
DLBE DeliverableBookEntry Deliverable, book entry.
TMPG TemporaryGlobal Deferred printing, global certificate.
GLOB Global Not deliverable, global certificate.
13.1.6.4.46.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Appearance expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.6.4.46.2  LegalForm <LglForm>
Presence: [0..1]
Definition: Specifies the form, ie, ownership, of the security.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 449 March 2024
```

