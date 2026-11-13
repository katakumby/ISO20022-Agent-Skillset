---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.20 FamilyInformation <FmlyInf>"]
file_pages: [5093]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.20 FamilyInformation <FmlyInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5093 to 5093.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5093

```text
66.1.32.7.20  FamilyInformation <FmlyInf>
Presence: [0..1]
Definition: Information related to the person.
FamilyInformation <FmlyInf> contains the following PersonalInformation1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NameOfFather <NmOfFthr> [0..1] Text 5093
   MaidenNameOfMother <MdnNmOfMthr> [0..1] Text 5093
   NameOfPartner <NmOfPrtnr> [0..1] Text 5093
66.1.32.7.20.1  NameOfFather <NmOfFthr>
Presence: [0..1]
Definition: Name of the father of the individual person.
Datatype: "Max35Text" on page 5403
66.1.32.7.20.2  MaidenNameOfMother <MdnNmOfMthr>
Presence: [0..1]
Definition: Maiden (unmarried) name of the mother of the individual person.
Datatype: "Max35Text" on page 5403
66.1.32.7.20.3  NameOfPartner <NmOfPrtnr>
Presence: [0..1]
Definition: Name of the partner of the individual person.
Datatype: "Max35Text" on page 5403
66.1.32.7.21  GDPRData <GDPRData>
Presence: [0..*]
Definition: Information about the individual's consent to use personal data under the General Protection
Regulation (GDPR) 2016/679 regulation.
GDPRData <GDPRData> contains the following GDPRData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConsentType <CnsntTp> [1..1]  5093
{Or     Code <Cd> [1..1] CodeSet 5094
Or}     Proprietary <Prtry> [1..1] ± 5094
   ConsentIndicator <CnsntInd> [1..1] Indicator 5094
   ConsentDate <CnsntDt> [1..1] Date 5095
66.1.32.7.21.1  ConsentType <CnsntTp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5093 May 2026
```

