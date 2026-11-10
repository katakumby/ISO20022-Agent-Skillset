---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.16 TransferCurrency <TrfCcy>"]
file_pages: [659, 660]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.16 TransferCurrency <TrfCcy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 659 to 660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 659

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
28.4.7.16  TransferCurrency <TrfCcy>
Presence: [0..1]
Definition: Currency to be used to transfer the holdings. Some transfer agents register holdings grouped
by currency in addition to using the ISIN for multi-currency fund shares.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 5276
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
28.4.7.17  OwnAccountTransferIndicator <OwnAcctTrfInd>
Presence: [0..1]
Definition: Indicates whether the transfer results in a change of beneficial owner.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
28.4.7.18  NonStandardSettlementInformation <NonStdSttlmInf>
Presence: [0..1]
Definition: Additional specific settlement information for the fund.
Datatype: "Max350Text" on page 5403
28.4.7.19  TransferExpensesPaymentType <TrfExpnssPmtTp>
Presence: [0..1]
Definition: Specifies how the payment of fees and taxes as a result of the transfer is covered, that is,
whether by cash or the redemption of units.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 659 May 2026
```

## File page 660

```text
TransferExpensesPaymentType <TrfExpnssPmtTp> contains one of the following elements (see
"ChargePaymentMethod1Choice" on page 4453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4453
Or}   Proprietary <Prtry> [1..1] ± 4453
28.4.8 AccountDetails <AcctDtls>
Presence: [1..1]
Definition: Information related to the account into which the financial instrument is to be received.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 660 May 2026
```

