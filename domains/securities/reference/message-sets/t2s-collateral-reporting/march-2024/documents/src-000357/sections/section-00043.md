---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.3 Financial Institution Identification", "4.1.3.2 BranchAndFinancialInstitutionIdentification8", "4.1.3.2.1 FinancialInstitutionIdentification <FinInstnId>"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.3.2.1 FinancialInstitutionIdentification <FinInstnId>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  47
     BICFI <BICFI> [0..1] IdentifierSet C4 47
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 48
     LEI <LEI> [0..1] IdentifierSet 48
     Name <Nm> [0..1] Text 48
     PostalAddress <PstlAdr> [0..1] ± 48
     Other <Othr> [0..1] ± 49
   BranchIdentification <BrnchId> [0..1]  50
     Identification <Id> [0..1] Text 50
     LEI <LEI> [0..1] IdentifierSet 50
     Name <Nm> [0..1] Text 50
     PostalAddress <PstlAdr> [0..1] ± 50
4.1.3.2.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C4 47
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 48
   LEI <LEI> [0..1] IdentifierSet 48
   Name <Nm> [0..1] Text 48
   PostalAddress <PstlAdr> [0..1] ± 48
   Other <Othr> [0..1] ± 49
4.1.3.2.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C4 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 79
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
47 March 2024
```

