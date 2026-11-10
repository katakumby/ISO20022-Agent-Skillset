---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.28 StaffClientBreakdown <StffClntBrkdwn>"]
file_pages: [1976, 1977]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.28 StaffClientBreakdown <StffClntBrkdwn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1976 to 1977.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1976

```text
Constraints
• TaxElementRule
One of the elements (TaxableIncomePerDividend, EUCapitalGain, EUDividendStatus,
PercentageOfDebtClaim, IndividualTax) must be present.
43.4.5.9.28  StaffClientBreakdown <StffClntBrkdwn>
Presence: [0..4]
Definition: Breakdown of the net amount per type of order.
StaffClientBreakdown <StffClntBrkdwn> contains the following elements (see
"InvestmentFundsOrderBreakdown2" on page 4733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OrderBreakdownType <OrdrBrkdwnTp> [1..1]  4733
{Or     Code <Cd> [1..1] CodeSet 4733
Or}     Proprietary <Prtry> [1..1] ± 4733
   Amount <Amt> [1..1] Amount C1, C13 4734
43.4.5.9.29  SettlementAndCustodyDetails <SttlmAndCtdyDtls>
Presence: [0..1]
Definition: Parameters used to execute the settlement of an investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1976 May 2026
```

## File page 1977

```text
SettlementAndCustodyDetails <SttlmAndCtdyDtls> contains the following
FundSettlementParameters22 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementDate <SttlmDt> [0..1] Date 1978
   SettlementPlace <SttlmPlc> [1..1]  1978
     Party <Pty> [1..1]  1979
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1979
Or       ProprietaryIdentification <PrtryId> [1..1] ± 1979
Or       NameAndAddress <NmAndAdr> [1..1] ± 1980
Or}       DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1980
     LEI <LEI> [0..1] IdentifierSet 1980
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1980
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1981
   TradeTransactionCondition <TradTxCond> [0..*] ± 1981
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1981
   ReceivingSideDetails <RcvgSdDtls> [1..1]  C33,
C34
1982
     ReceiversCustodianDetails <RcvrsCtdnDtls> [0..1]  1983
       PartyIdentification <PtyId> [1..1] ± 1983
       AccountIdentification <AcctId> [0..1] Text 1983
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1983
     ReceiversIntermediary1Details <RcvrsIntrmy1Dtls> [0..1]  1984
       PartyIdentification <PtyId> [1..1] ± 1984
       AccountIdentification <AcctId> [0..1] Text 1984
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1984
     ReceiversIntermediary2Details <RcvrsIntrmy2Dtls> [0..1]  1985
       PartyIdentification <PtyId> [1..1] ± 1985
       AccountIdentification <AcctId> [0..1] Text 1985
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1985
     ReceivingAgentDetails <RcvgAgtDtls> [1..1]  1986
       PartyIdentification <PtyId> [1..1] ± 1986
       AccountIdentification <AcctId> [0..1] Text 1986
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1986
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1977 May 2026
```

