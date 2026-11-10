---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.3 IndividualPerson37", "66.1.32.3.20 FamilyInformation <FmlyInf>", "66.1.32.3.20.2 MaidenNameOfMother <MdnNmOfMthr>"]
file_pages: [5073]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.3.20.2 MaidenNameOfMother <MdnNmOfMthr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5073 to 5073.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5073

```text
66.1.32.3.20.2  MaidenNameOfMother <MdnNmOfMthr>
Presence: [0..1]
Definition: Maiden (unmarried) name of the mother of the individual person.
Datatype: "Max35Text" on page 5403
66.1.32.3.20.3  NameOfPartner <NmOfPrtnr>
Presence: [0..1]
Definition: Name of the partner of the individual person.
Datatype: "Max35Text" on page 5403
66.1.32.3.21  GDPRData <GDPRData>
Presence: [0..*]
Definition: Information about the individual's consent to use personal data under the General Protection
Regulation (GDPR) 2016/679 regulation.
GDPRData <GDPRData> contains the following GDPRData1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConsentType <CnsntTp> [1..1]  5073
{Or     Code <Cd> [1..1] CodeSet 5073
Or}     Proprietary <Prtry> [1..1] ± 5074
   ConsentIndicator <CnsntInd> [1..1] Indicator 5074
   ConsentDate <CnsntDt> [1..1] Date 5074
66.1.32.3.21.1  ConsentType <CnsntTp>
Presence: [1..1]
Definition: Type of consent.
ConsentType <CnsntTp> contains one of the following GDPRDataConsent1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5073
Or}   Proprietary <Prtry> [1..1] ± 5074
66.1.32.3.21.1.1  Code <Cd>
Presence: [1..1]
Definition: Consent type expressed as a code.
Datatype: "GDPRDataConsent1Code" on page 5307
CodeName Name Definition
DP00 ConsentMarketing Consent to authorise the controller of
personal data processing to process
personal data for marketing purposes.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5073 May 2026
```

