---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.13 SafekeepingAccount2", "66.1.24.13.7 AccountServicer <AcctSvcr>"]
file_pages: [4645, 4646]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.13.7 AccountServicer <AcctSvcr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4645 to 4646.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4645

```text
66.1.24.13.7  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains one of the following elements (see "PartyIdentification2Choice"
on page 4887 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4887
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4888
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4888
66.1.24.14  InvestmentAccount75
Definition: Information about a securities account and its characteristics.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4645 May 2026
```

## File page 4646

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountStatusUpdateInstruction <AcctStsUpdInstr> [0..1] ± 4647
   Name <Nm> [0..1] Text 4648
   Designation <Dsgnt> [0..1] Text 4648
   Type <Tp> [0..1] ± 4648
   OwnershipType <OwnrshTp> [0..1] ± 4649
   TaxExemption <TaxXmptn> [0..1] ± 4649
   StatementFrequency <StmtFrqcy> [0..1] ± 4649
   ReferenceCurrency <RefCcy> [0..1] CodeSet C1 4649
   Language <Lang> [0..1] CodeSet C34 4650
   IncomePreference <IncmPref> [0..1] CodeSet 4650
   ReinvestmentDetails <RinvstmtDtls> [0..*] ± 4650
   TaxWithholdingMethod <TaxWhldgMtd> [0..1] CodeSet 4650
   TaxReporting <TaxRptg> [0..*] ± 4651
   LetterIntentDetails <LttrInttDtls> [0..1] ± 4652
   AccumulationRightReference <AcmltnRghtRef> [0..1] Text 4653
   RequiredSignatoriesNumber <ReqrdSgntriesNb> [0..1] Quantity 4653
   FundFamilyName <FndFmlyNm> [0..1] Text 4653
   ModifiedFinancialInstrumentDetails
<ModfdFinInstrmDtls>
[0..*]  4653
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4653
     FinancialInstrumentDetails <FinInstrmDtls> [1..1] ± C20 4654
   RoundingDetails <RndgDtls> [0..1] ± 4655
   AccountServicer <AcctSvcr> [0..1] ± 4655
   BlockedStatus <BlckdSts> [0..1] ± 4655
   AccountUsageType <AcctUsgTp> [0..1] ± 4656
   ForeignStatusCertification <FrgnStsCertfctn> [0..1] CodeSet 4656
   AccountSignatureDateTime <AcctSgntrDtTm> [0..1] ± 4656
   TransactionChannelType <TxChanlTp> [0..1] ± 4657
   InvestmentAccountCategory <InvstmtAcctCtgy> [0..1] ± 4657
   Pledging <Pldgg> [0..1] CodeSet 4657
   Collateral <Coll> [0..1] CodeSet 4657
   ThirdPartyRights <ThrdPtyRghts> [0..1] ± 4658
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4646 May 2026
```

