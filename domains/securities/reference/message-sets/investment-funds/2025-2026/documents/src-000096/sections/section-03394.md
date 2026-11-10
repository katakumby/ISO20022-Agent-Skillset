---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.10 InvestmentAccount76", "66.1.24.10.6 AccountOwner <AcctOwnr>", "66.1.24.10.6.1 IndividualOwnerIdentification <IndvOwnrId>"]
file_pages: [4638]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.10.6.1 IndividualOwnerIdentification <IndvOwnrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4638 to 4638.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4638

```text
AccountOwner <AcctOwnr> contains one of the following AccountOwner3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndividualOwnerIdentification <IndvOwnrId> [1..1]  4638
{Or     IdentificationNumber <IdNb> [1..1] ± 4638
Or}     PersonName <PrsnNm> [1..1] ± 4638
Or}   OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± C21 4639
66.1.24.10.6.1  IndividualOwnerIdentification <IndvOwnrId>
Presence: [1..1]
Definition: Identification of the individual person that legally owns the account.
IndividualOwnerIdentification <IndvOwnrId> contains one of the following
IndividualPersonIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IdentificationNumber <IdNb> [1..1] ± 4638
Or}   PersonName <PrsnNm> [1..1] ± 4638
66.1.24.10.6.1.1  IdentificationNumber <IdNb>
Presence: [1..1]
Definition: Identification of the person that owns the account.
IdentificationNumber <IdNb> contains the following elements (see "GenericIdentification81" on
page 4543 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4544
   IdentificationType <IdTp> [1..1]  4544
{Or     Code <Cd> [1..1] CodeSet 4544
Or}     Proprietary <Prtry> [1..1] ± 4545
66.1.24.10.6.1.2  PersonName <PrsnNm>
Presence: [1..1]
Definition: Name of the person that owns the account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4638 May 2026
```

