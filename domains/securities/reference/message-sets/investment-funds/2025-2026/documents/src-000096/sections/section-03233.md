---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.14 Date Time Period", "66.1.14.1 TimeHorizon2Choice", "66.1.14.1.2 TimeFrame <TmFrame>", "66.1.14.1.2.1 Code <Cd>"]
file_pages: [4469]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.14.1.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4469 to 4469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4469

```text
Definition: Time frame as a qualitative value.
TimeFrame <TmFrame> contains one of the following TimeFrame9Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4469
Or}   Proprietary <Prtry> [1..1] ± 4469
66.1.14.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Time frame expressed as a code.
Datatype: "TimeFrame2Code" on page 5377
CodeName Name Definition
HOLD Hold Hold to maturity.
LONG LongTerm Greater than five years.
MEDM MediumTerm Greater than or equal to three years.
SHOR ShortTerm Greater than or equal to one year.
VSHT VeryShortTerm Less than one year.
66.1.14.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Time frame expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.14.2  TimeFrame9
Definition: Time frame elements that define a period as number of days before or after a activity.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherTimeFrameDescription <OthrTmFrameDesc> [0..1] Text 4470
   TradeMinus <TMns> [0..1] Quantity 4470
   NonWorkingDayAdjustment <NonWorkgDayAdjstmnt> [0..1] CodeSet 4470
   ReferToOrderDesk <RefrToOrdrDsk> [0..1] CodeSet 4470
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4469 May 2026
```

