---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.3 CommonFinancialInstrumentAttributes11", "13.1.6.3.45 FinancialInstrumentForm <FinInstrmForm>", "13.1.6.3.45.1 BookingAppearance <BookgApprnc>", "13.1.6.3.45.1.2 Proprietary <Prtry>"]
file_pages: [374]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.3.45.1.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 374 to 374.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 374

```text
CodeName Name Definition
BENT BookEntry Security exists only as an electronic
record, ie, there are no physical
certificates representing the security.
DFBE DeferredBookEntry Deferred printing, book entry.
DLBE DeliverableBookEntry Deliverable, book entry.
TMPG TemporaryGlobal Deferred printing, global certificate.
GLOB Global Not deliverable, global certificate.
13.1.6.3.45.1.2  Proprietary <Prtry>
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
13.1.6.3.45.2  LegalForm <LglForm>
Presence: [0..1]
Definition: Specifies the form, ie, ownership, of the security.
LegalForm <LglForm> contains one of the following elements (see "FormOfSecurity8Choice" on
page 482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 482
Or}   Proprietary <Prtry> [1..1] ± 482
13.1.6.3.46  ContactName <CtctNm>
Presence: [0..1]
Definition: Details (name, e-mail address and/or telephone number) of the person requesting the
allocation of the ISIN used as a point of reference in case further clarifications are required.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 374 March 2024
```

