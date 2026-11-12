---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.1.2.47 FinancialInstrumentForm <FinInstrmForm>", "28.4.2.1.1.2.47.1 BookingAppearance <BookgApprnc>", "28.4.2.1.1.2.47.1.1 Code <Cd>"]
file_pages: [1161]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.2.47.1.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1161 to 1161.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1161

```text
BookingAppearance <BookgApprnc> contains one of the following Appearance3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1161
Or}   Proprietary <Prtry> [1..1] ± 1161
28.4.2.1.1.2.47.1.1  Code <Cd>
Presence: [1..1]
Definition: Appearance expressed as an ISO 20022 code.
Datatype: "Appearance1Code" on page 3213
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
28.4.2.1.1.2.47.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Appearance expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.1.2.47.2  LegalForm <LglForm>
Presence: [0..1]
Definition: Specifies the form, ie, ownership, of the security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1161 August 2026
```

