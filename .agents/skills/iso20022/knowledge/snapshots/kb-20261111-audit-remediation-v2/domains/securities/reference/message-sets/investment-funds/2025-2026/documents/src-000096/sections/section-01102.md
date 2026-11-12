---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.5 Portfolio <Prtfl>", "40.4.15.5.1 TaxEfficientProduct <TaxEffcntPdct>", "40.4.15.5.1.9 BonusOrWithdrawal <BnsOrWdrwl>", "40.4.15.5.1.9.5 Outstanding <Outsdng>"]
file_pages: [1545]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.5.1.9.5 Outstanding <Outsdng>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1545 to 1545.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1545

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
40.4.15.5.1.9.5  Outstanding <Outsdng>
Presence: [0..1]
Definition: Indicates whether there is an outstanding bonus or withdrawal amount.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.5.1.9.6  Reference <Ref>
Presence: [0..1]
Definition: Identification of the withdrawal or bonus.
Datatype: "Max35Text" on page 5403
40.4.15.5.1.9.7  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the monies paid out or withdrawn.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
40.4.15.5.1.10  WithdrawalForResidentialPurchaseProgress <WdrwlForResdtlPurchsPrgrs>
Presence: [0..1]
Definition: Indicates if there is a related property purchase in progress at the point of transfer. May be
applicable to products such as Lifetime Individual Savings Account (LISA) products.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
40.4.15.5.1.11  TransferorAlternateIdentification <TrfrAltrnId>
Presence: [0..1]
Definition: Alternative identification for the transferor (ceding party), for example, the 'ISA manager Z
reference' in the UK.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1545 May 2026
```

