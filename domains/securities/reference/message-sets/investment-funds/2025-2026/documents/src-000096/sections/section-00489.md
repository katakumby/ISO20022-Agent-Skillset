---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.8.14 SettlementPartiesDetails <SttlmPtiesDtls>", "28.4.8.14.4 ReceivingSideDetails <RcvgSdDtls>", "28.4.8.14.4.1 Depository <Dpstry>"]
file_pages: [668]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.8.14.4.1 Depository <Dpstry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 668 to 668.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 668

```text
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
• SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
28.4.8.14.4.1  Depository <Dpstry>
Presence: [0..1]
Definition: First party in the settlement chain. In a plain vanilla settlement, it is the Central Securities
Depository where the counterparty requests to receive the financial instrument or from where the
counterparty delivers the financial instruments. This party may be a transfer agent.
Depository <Dpstry> contains the following elements (see "PartyIdentification315" on page 4906 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1]  4906
{Or     AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4907
Or     NameAndAddress <NmAndAdr> [1..1] ± 4907
Or     Country <Ctry> [1..1] CodeSet C12 4907
Or}     DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 4908
   LEI <LEI> [0..1] IdentifierSet 4908
   AlternateIdentification <AltrnId> [0..1] ± 4908
   ProcessingDate <PrcgDt> [0..1] ± 4908
   ProcessingIdentification <PrcgId> [0..1] Text 4908
   AdditionalInformation <AddtlInf> [0..1] ± C3 4909
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 668 May 2026
```

