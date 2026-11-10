---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.1 Identification <Id>", "15.4.5.8.1.1 OtherIdentification <OthrId>"]
file_pages: [313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.1.1 OtherIdentification <OthrId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 313 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 313

```text
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
15.4.5.8.1.1  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 313
   Suffix <Sfx> [0..1] Text 313
   Type <Tp> [1..1] ± 313
15.4.5.8.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 5403
15.4.5.8.1.1.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 5402
15.4.5.8.1.1.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 4550 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4550
Or}   Proprietary <Prtry> [1..1] Text 4550
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 313 May 2026
```

