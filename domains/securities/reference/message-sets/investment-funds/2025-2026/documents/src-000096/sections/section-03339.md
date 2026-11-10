---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.4 InvestmentAccountOwnershipInformation17", "66.1.24.4.2 MoneyLaunderingCheck <MnyLndrgChck>"]
file_pages: [4580]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.4.2 MoneyLaunderingCheck <MnyLndrgChck>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4580 to 4580.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4580

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DeathDate <DthDt> [0..1] Date 5091
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
66.1.24.4.2  MoneyLaunderingCheck <MnyLndrgChck>
Presence: [0..1]
Definition: Status of an identity check to prevent money laundering. This includes the counter-terrorism
check.
MoneyLaunderingCheck <MnyLndrgChck> contains one of the following elements (see
"MoneyLaunderingCheck1Choice" on page 4922 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4923
Or}   Proprietary <Prtry> [1..1] ± 4923
66.1.24.4.3  ModifiedInvestorProfileValidation <ModfdInvstrPrflVldtn>
Presence: [0..*]
Definition: Information related to the party profile to be inserted or deleted.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4580 May 2026
```

