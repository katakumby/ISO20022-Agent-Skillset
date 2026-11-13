---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.8 InvestmentAccountDetails <InvstmtAcctDtls>", "46.4.5.8.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [2350]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.8.8 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2350 to 2350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2350

```text
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount6" on
page 4642 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4642
   Name <Nm> [0..1] Text 4642
   Characteristic <Chrtc> [0..1] Text 4642
   AccountDesignation <AcctDsgnt> [0..1] Text 4642
46.4.5.8.8  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
46.4.5.9  BeneficiaryDetails <BnfcryDtls>
Presence: [0..*]
Definition: Additional information about the investor.
Impacted by: C29 "PersonElementRule"
BeneficiaryDetails <BnfcryDtls> contains the following elements (see "IndividualPerson32" on
page 5075 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5076
   BirthDate <BirthDt> [0..1] Date 5076
   CountryAndResidentialStatus <CtryAndResdtlSts> [0..1] ± 5076
   OtherIdentification <OthrId> [0..*]  5076
     Identification <Id> [1..1] Text 5077
     IdentificationType <IdTp> [1..1]  5077
{Or       Code <Cd> [1..1] CodeSet 5077
Or}       Proprietary <Prtry> [1..1] ± 5078
     Issuer <Issr> [0..1] Text 5078
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2350 May 2026
```

