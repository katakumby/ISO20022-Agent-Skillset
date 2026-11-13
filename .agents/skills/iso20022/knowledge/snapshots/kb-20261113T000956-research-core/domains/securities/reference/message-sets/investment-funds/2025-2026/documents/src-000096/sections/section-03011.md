---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "57.4 Message Building Blocks", "57.4.3 StatusReport <StsRpt>", "57.4.3.1 CancellationStatusReport <CxlStsRpt>", "57.4.3.1.3 StatusInitiator <StsInitr>"]
file_pages: [4216, 4217]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.017.001.05"]
---

# 57.4.3.1.3 StatusInitiator <StsInitr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4216 to 4217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4216

```text
57.4.3.1.3  StatusInitiator <StsInitr>
Presence: [0..1]
Definition: Party that initiates the status of the order cancellation.
StatusInitiator <StsInitr> contains the following elements (see "PartyIdentification139" on page 5043
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
57.4.3.2  IndividualCancellationStatusReport <IndvCxlStsRpt>
Presence: [1..*]
Definition: Status report details of one or more individual orders from a bulk or multiple or switch order
cancellation request.
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4216 May 2026
```

## File page 4217

```text
IndividualCancellationStatusReport <IndvCxlStsRpt> contains the following
IndividualOrderStatusAndReason10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 4218
   OrderReference <OrdrRef> [1..1] Text 4218
   ClientReference <ClntRef> [0..1] Text 4219
   NonceIdentification <NonceId> [0..1] Text 4219
   CancellationReference <CxlRef> [0..1] Text 4219
   CancellationStatus <CxlSts> [1..1]  4219
{Or     Status <Sts> [1..1] CodeSet 4219
Or}     Rejected <Rjctd> [1..1]  C8 4220
       Reason <Rsn> [0..1]  4220
{Or         Code <Cd> [1..1] CodeSet 4220
Or}         Proprietary <Prtry> [1..1] ± 4221
       AdditionalInformation <AddtlInf> [0..1] Text 4221
   StatusInitiator <StsInitr> [0..1] ± 4221
   InvestmentAccountDetails <InvstmtAcctDtls> [0..1]  C6 4222
     AccountIdentification <AcctId> [1..1] Text 4222
     AccountName <AcctNm> [0..1] Text 4222
     AccountDesignation <AcctDsgnt> [0..1] Text 4222
     OwnerIdentification <OwnrId> [0..*] ± 4223
     AccountServicer <AcctSvcr> [0..1] ± 4223
     OrderOriginatorEligibility <OrdrOrgtrElgblty> [0..1] CodeSet 4223
     SubAccountDetails <SubAcctDtls> [0..1] ± 4223
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 4224
   FinancialInstrumentDetails <FinInstrmDtls> [0..1]  C4 4224
     Identification <Id> [1..1]  4226
{Or       ISIN <ISIN> [1..1] IdentifierSet 4226
Or       SEDOL <SEDOL> [1..1] IdentifierSet 4227
Or       CUSIP <CUSIP> [1..1] IdentifierSet 4227
Or       RIC <RIC> [1..1] IdentifierSet 4227
Or       TickerSymbol <TckrSymb> [1..1] IdentifierSet 4227
Or       Bloomberg <Blmbrg> [1..1] IdentifierSet 4227
Approved by the Securities SEG on 27 January 2026 setr.017.001.05 OrderCancellationStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4217 May 2026
```

