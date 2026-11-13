---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: []
content_origin: "source-transcription"
---

# Publication front matter

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1** ISO 20022

**P2** Settlement and Reconciliation - Maintenance 2025 - 2026

**P4** Message Definition Report - Part 1

**P5** Approved by the Securities SEG on 27 January 2026

**P6** This document provides information about the use of the messages for Settlement and Reconciliation and includes, for example, business scenarios and messages flows.

**P7** March 2026

**P8** Table of Contents

**P9** Table of Contents	2

**P10** 1	Introduction	5

**P11** 1.1	Terms and Definitions	5

**P12** 1.2	Abbreviations and Acronyms	5

**P13** 1.3	Document Scope and Objectives	5

**P14** 1.4	References	6

**P15** 2	Scope and Functionality	7

**P16** 2.1	Background	7

**P17** 2.2	Scope	8

**P18** 2.3	Groups of MessageDefinitions and Functionality	9

**P19** 3	BusinessRoles and Participants	12

**P20** 3.1	Participants and BusinessRoles Definitions	13

**P21** 3.2	BusinessRoles and Participants Table	14

**P22** 4	BusinessProcess Description	15

**P23** 5	Description of BusinessActivities	19

**P24** 5.1	Instruction and Confirmation - Typical Process	19

**P25** 5.2	Intra-Position Instruction Process	21

**P26** 5.3	Partial Settlement Confirmation	22

**P27** 5.4	Securities Financing Instruction	23

**P28** 5.5	Pair-off Instruction	32

**P29** 5.6	Cash/Securities Split Instruction and Confirmation Process	33

**P30** 5.7	Status Reporting Process	35

**P31** 5.8	Modification Process	38

**P32** 5.9	Split Settlement Process	45

**P33** 5.10	Allegement Process	46

**P34** 5.11	Reconciliation and Reporting Process	47

**P35** 5.12	Cancellation Request Process	51

**P36** 5.13	Cancellation Advise Process	52

**P37** 5.14	Reversal Advice Process	53

**P38** 5.15	Portfolio Transfer Process	54

**P39** 5.16	Transaction Generation Process	55

**P40** 6	BusinessTransactions	56

**P41** 6.1	Instruction and Confirmation	56

**P42** 6.2	Intra-Position Instruction	57

**P43** 6.3	Partial Settlement Confirmation	57

**P44** 6.4	Securities Financing	58

**P45** 6.5	Pair-Off Instruction	69

**P46** 6.6	Cash/Securities Split Instruction and Confirmation	70

**P47** 6.7	Status Reporting	71

**P48** 6.8	Modification	71

**P49** 6.9	Split Settlement	79

**P50** 6.10	Allegement	87

**P51** 6.11	Reconciliation and Reporting	87

**P52** 6.12	Cancellation Request	90

**P53** 6.13	Cancellation Advice	91

**P54** 6.14	Reversal Advice	92

**P55** 6.15	Portfolio Transfer	92

**P56** 6.16	Transaction Generation	93

**P57** 7	Business Examples	94

**P58** 7.1	SecuritiesBalanceCustodyReport semt.002.001.12	94

**P59** 7.2	SecuritiesBalanceAccountingReport semt.003.001.12	97

**P60** 7.3	IntraPositionMovementInstruction semt.013.001.07	102

**P61** 7.4	IntraPositionMovementStatusAdvice semt.014.001.09	103

**P62** 7.5	IntraPositionMovementConfirmation semt.015.001.10	104

**P63** 7.6	IntraPositionMovementPostingReport semt.016.001.10	105

**P64** 7.7	SecuritiesTransactionPostingReport semt.017.001.14	107

**P65** 7.8	SecuritiesTransactionPendingReport semt.018.001.15	110

**P66** 7.9	SecuritiesSettlementTransactionAllegementReport semt.019.001.12	114

**P67** 7.10	SecuritiesMessageCancellationAdvice semt.020.001.07	117

**P68** 7.11	SecuritiesStatementQuery semt.021.001.09	117

**P69** 7.12	SecuritiesSettlementTransactionAuditTrailReport semt.022.001.07	119

**P70** 7.13	SecuritiesTransactionCancellationRequest sese.020.001.09	120

**P71** 7.14	SecuritiesTransactionStatusQuery sese.021.001.08	122

**P72** 7.15	SecuritiesStatusOrStatementQueryStatusAdvice sese.022.001.08	123

**P73** 7.16	SecuritiesSettlementTransactionInstruction sese.023.001.13	124

**P74** 7.17	SecuritiesSettlementTransactionStatusAdvice sese.024.001.14	127

**P75** 7.18	SecuritiesSettlementTransactionConfirmation sese.025.001.13	129

**P76** 7.19	SecuritiesSettlementTransactionReversalAdvice sese.026.001.12	132

**P77** 7.20	SecuritiesTransactionCancellationRequestStatusAdvice sese.027.001.09	135

**P78** 7.21	SecuritiesSettlementTransactionAllegementNotification sese.028.001.12	137

**P79** 7.22	SecuritiesSettlementAllegementRemovalAdvice sese.029.001.08	139

**P80** 7.23	SecuritiesSettlementConditionsModificationRequest sese.030.001.10	142

**P81** 7.24	SecuritiesSettlementConditionsStatusAdvice sese.031.001.11	142

**P82** 7.25	SecuritiesSettlementTransactionGenerationNotification sese.032.001.13	143

**P83** 7.26	SecuritiesFinancingInstruction sese.033.001.13	146

**P84** 7.27	SecuritiesFinancingStatusAdvice sese.034.001.11	148

**P85** 7.28	SecuritiesFinancingConfirmation sese.035.001.13	150

**P86** 7.29	SecuritiesFinancingModificationInstruction sese.036.001.10	153

**P87** 7.30	PortfolioTransferNotification sese.037.001.09	155

**P88** 7.31	SecuritiesSettlementTransactionModificationRequest sese.038.001.11	162

**P89** 7.32	SecuritiesSettlementTransactionModificationRequestStatusAdvice sese.039.001.08	163

**P90** 7.33	SecuritiesSettlementTransactionCounterpartyResponse sese.040.001.06	164

**P91** Revision Record	165

**P93** Preliminary note:

**P94** The Message Definition Report (MDR) is made of three parts:

**P95** - MDR - Part 1 describes the contextual background required to understand the functionality of the proposed message set. Part 1 is produced by the submitting organisation that developed or maintained the message set in line with a MDR Part1 template provided by the ISO 20022 Registration Authority (RA) on www.iso20022.org

**P97** - MDR – Part 2 is the detailed description of each message definition of the message set. Part 2 is produced by the RA using the model developed by the submitting organisation.

**P99** - MDR – Part 3 is an extract of the ISO 20022 Business Model describing the business concepts used in the message set. Part 3 is an Excel document produced by the RA.

