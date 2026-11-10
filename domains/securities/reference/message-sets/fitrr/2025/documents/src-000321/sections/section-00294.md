---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.10 Party Identification", "22.1.10.2 PartyIdentification76", "22.1.10.2.2 CountryOfBranch <CtryOfBrnch>"]
file_pages: [344]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.10.2.2 CountryOfBranch <CtryOfBrnch>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 344 to 344.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 344

```text
Datatype: "InternalPartyRole1Code" on page 438
CodeName Name Definition
INTC Internal Party acting as an internal agent.
22.1.10.2.2  CountryOfBranch <CtryOfBrnch>
Presence: [0..1]
Definition: Country of the branch that received the order from the client or made an investment decision
for a client in accordance with a discretionary mandate given to it by the client.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.1.10.3  PartyIdentification79
Definition: Set of elements used to identify an account owner and the associated decision maker.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [1..*] ± 344
   DecisionMaker <DcsnMakr> [0..*]  345
{Or     LEI <LEI> [1..1] IdentifierSet 345
Or}     Person <Prsn> [1..1] ± 345
22.1.10.3.1  AccountOwner <AcctOwnr>
Presence: [1..*]
Definition: Identifies the account which is used to acquire or sell financial instruments.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification76" on page 342
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  342
{Or     LEI <LEI> [1..1] IdentifierSet 343
Or     MIC <MIC> [1..1] IdentifierSet 343
Or     Person <Prsn> [1..1] ± 343
Or}     Internal <Intl> [1..1] CodeSet 343
   CountryOfBranch <CtryOfBrnch> [0..1] CodeSet C4 344
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
344 July 2025
```

