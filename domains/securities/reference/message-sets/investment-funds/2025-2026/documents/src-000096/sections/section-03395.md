---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.10 InvestmentAccount76", "66.1.24.10.6 AccountOwner <AcctOwnr>", "66.1.24.10.6.2 OrganisationOwnerIdentification <OrgOwnrId>"]
file_pages: [4639]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.10.6.2 OrganisationOwnerIdentification <OrgOwnrId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4639 to 4639.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4639

```text
PersonName <PrsnNm> contains the following elements (see "IndividualPerson35" on page 5061 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GivenName <GvnNm> [0..1] Text 5062
   MiddleName <MddlNm> [0..1] Text 5062
   Name <Nm> [1..1] Text 5062
   Gender <Gndr> [0..1] CodeSet 5062
   BirthDate <BirthDt> [0..1] Date 5062
66.1.24.10.6.2  OrganisationOwnerIdentification <OrgOwnrId>
Presence: [1..1]
Definition: Identification of the organisation that legally owns the account.
Impacted by: C21 "OrganisationIdentificationRule"
OrganisationOwnerIdentification <OrgOwnrId> contains the following elements (see
"PartyIdentification220" on page 4900 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1]  4901
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4901
Or     ProprietaryIdentification <PrtryId> [1..1] ± 4902
Or     NameAndAddress <NmAndAdr> [1..1]  4902
       Name <Nm> [1..1] Text 4902
       PostalAddress <PstlAdr> [0..1] ± C23 4902
Or     TaxIdentificationNumber <TaxIdNb> [1..1] Text 4903
Or}     NationalRegistrationNumber <NtlRegnNb> [1..1] Text 4903
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4904
Constraints
• OrganisationIdentificationRule
Either Identification or Legal Entity Identifier must be present. Both Identification and Legal Entity
Identifier may be present.
Following Must be True
    /Identification Must be present
 Or    /LegalEntityIdentifier Must be present
66.1.24.10.7  Intermediary <Intrmy>
Presence: [0..*]
Definition: Intermediary or other party related to the management of the account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4639 May 2026
```

