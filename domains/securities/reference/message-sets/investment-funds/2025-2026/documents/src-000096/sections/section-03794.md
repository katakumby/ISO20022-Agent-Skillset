---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.7 IndividualPerson38", "66.1.32.7.1 NamePrefix <NmPrfx>"]
file_pages: [5083]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.7.1 NamePrefix <NmPrfx>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5083 to 5083.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5083

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CivilStatus <CvlSts> [0..1]  5092
{Or     Code <Cd> [1..1] CodeSet 5092
Or}     Proprietary <Prtry> [1..1] ± 5092
   EducationLevel <EdctnLvl> [0..1] Text 5092
   FamilyInformation <FmlyInf> [0..1]  5093
     NameOfFather <NmOfFthr> [0..1] Text 5093
     MaidenNameOfMother <MdnNmOfMthr> [0..1] Text 5093
     NameOfPartner <NmOfPrtnr> [0..1] Text 5093
   GDPRData <GDPRData> [0..*]  5093
     ConsentType <CnsntTp> [1..1]  5093
{Or       Code <Cd> [1..1] CodeSet 5094
Or}       Proprietary <Prtry> [1..1] ± 5094
     ConsentIndicator <CnsntInd> [1..1] Indicator 5094
     ConsentDate <CnsntDt> [1..1] Date 5095
66.1.32.7.1  NamePrefix <NmPrfx>
Presence: [0..1]
Definition: Term used to address the person.
NamePrefix <NmPrfx> contains one of the following NamePrefix1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5083
Or}   Proprietary <Prtry> [1..1] ± 5084
66.1.32.7.1.1  Code <Cd>
Presence: [1..1]
Definition: Name prefix expressed as a code.
Datatype: "NamePrefix1Code" on page 5330
CodeName Name Definition
DOCT Doctor Title of the person is Doctor or Dr.
MIST Mister Title of the person is Mister or Mr.
MISS Miss Title of the person is Miss.
MADM Madam Title of the person is Madam.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5083 May 2026
```

