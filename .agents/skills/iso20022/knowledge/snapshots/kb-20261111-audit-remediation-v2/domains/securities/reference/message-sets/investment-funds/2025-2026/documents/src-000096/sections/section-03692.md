---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.14 FATCAStatus2"]
file_pages: [4960]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.14 FATCAStatus2

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4960 to 4960.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4960

```text
Definition: Additional information about the main order desk.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
66.1.30.14  FATCAStatus2
Definition: Foreign Account Tax Compliance Act (FATCA) status information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  4960
{Or     Code <Cd> [1..1] CodeSet 4960
Or}     Proprietary <Prtry> [1..1] ± 4961
   Source <Src> [0..1]  4961
{Or     Code <Cd> [1..1] CodeSet 4962
Or}     Proprietary <Prtry> [1..1] ± 4962
66.1.30.14.1  Type <Tp>
Presence: [1..1]
Definition: Foreign Account Tax Compliance Act (FATCA) status.
Type <Tp> contains one of the following FATCAStatus2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4960
Or}   Proprietary <Prtry> [1..1] ± 4961
66.1.30.14.1.1  Code <Cd>
Presence: [1..1]
Definition: Foreign Account Tax Compliance Act (FATCA) status expressed as a code.
Datatype: "FATCAStatus1Code" on page 5301
CodeName Name Definition
F101 FATCA101 Account holder type is an owner-
documented financial institution with
specified US owner(s).
F102 FATCA102 Account holder type is a passive non-
financial entity with substantial US
owner(s).
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4960 May 2026
```

